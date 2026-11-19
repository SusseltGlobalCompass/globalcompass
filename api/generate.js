const ALLOWED_ORIGINS = [
  "https://globalcompass.education",
  "https://www.globalcompass.education"
];
const MAX_PROMPT_CHARS = 8000;
const MAX_TOKENS_CAP = 3500;

export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  // Only accept requests that come from the GlobalCompass website itself
  const origin = req.headers.origin || "";
  if (!ALLOWED_ORIGINS.includes(origin)) {
    res.status(403).json({ error: "Forbidden" });
    return;
  }

  try {
    const body = req.body || {};
    const prompt = body.prompt;

    if (typeof prompt !== "string" || prompt.length === 0) {
      res.status(400).json({ error: "Missing prompt" });
      return;
    }
    if (prompt.length > MAX_PROMPT_CHARS) {
      res.status(413).json({ error: "Prompt too long" });
      return;
    }

    const requested = Number(body.max_tokens) || 1400;
    const max_tokens = Math.min(Math.max(requested, 100), MAX_TOKENS_CAP);

    const response = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": process.env.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-6",
        max_tokens,
        messages: [{ role: "user", content: prompt }]
      })
    });

    const data = await response.json();

    if (!response.ok) {
      console.error("Anthropic API error:", data);
      const msg = (data.error && data.error.message) || "API request failed";
      res.status(response.status).json({ error: msg });
      return;
    }

    res.status(200).json(data);
  } catch (error) {
    console.error("Server error:", error);
    res.status(500).json({ error: "Internal server error" });
  }
}
