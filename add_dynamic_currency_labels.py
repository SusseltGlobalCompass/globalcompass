"""
Make the budget dropdown show real local-currency amounts when a search
is scoped to a single country (e.g. "Under AED 20,200/yr" for UAE),
falling back to USD when the search isn't country-specific. The actual
filtering logic underneath stays USD-based and untouched - this only
changes what the visitor SEES.

Run from inside ~/Desktop/GlobalCompass
"""

FILE = "schools.html"

with open(FILE, "r", encoding="utf-8") as f:
    content = f.read()

original = content

old_anchor = '''  return data ? data.map(c => c.id) : [];
}

async function runSearch(){'''

new_anchor = '''  return data ? data.map(c => c.id) : [];
}

let currencyRatesPromise = null;
function ensureCurrencyRates(){
  if(!currencyRatesPromise){
    currencyRatesPromise = sb.from("currency_rates").select("currency_code, rate_to_usd").then(({data}) => {
      const map = {};
      if(data) data.forEach(r => { map[r.currency_code] = r.rate_to_usd; });
      return map;
    });
  }
  return currencyRatesPromise;
}

function fmtLocal(usdAmt, rate, code){
  const local = Math.round(usdAmt * rate / 100) * 100;
  return code + " " + local.toLocaleString();
}

function updateBudgetLabels(currencyCode, ratesMap){
  const sel = document.getElementById("budgetSel");
  const opts = sel.options;
  const rate = (currencyCode && ratesMap) ? ratesMap[currencyCode] : null;
  if(rate){
    opts[1].textContent = "Under " + fmtLocal(5500, rate, currencyCode) + "/yr";
    opts[2].textContent = fmtLocal(5500, rate, currencyCode) + "\\u2013" + fmtLocal(12000, rate, currencyCode) + "/yr";
    opts[3].textContent = fmtLocal(12000, rate, currencyCode) + "\\u2013" + fmtLocal(20000, rate, currencyCode) + "/yr";
    opts[4].textContent = fmtLocal(20000, rate, currencyCode) + "+/yr";
  } else {
    opts[1].textContent = "Under $5,500/yr";
    opts[2].textContent = "$5,500\\u2013$12,000/yr";
    opts[3].textContent = "$12,000\\u2013$20,000/yr";
    opts[4].textContent = "$20,000+/yr";
  }
}

async function runSearch(){'''

if old_anchor not in content:
    print("ERROR: Could not find anchor point for helper functions. No changes made.")
else:
    content = content.replace(old_anchor, new_anchor)

    old_block = '''  if(q){
    const countryIds = await resolveCountryIds(q);
    if(countryIds.length){
      // The search term matched a real country name exactly - filter by
      // country only, skip the expensive name/city fuzzy search entirely.
      query = query.in("country_id", countryIds);
      hintEl.textContent = 'Tip: for more specific results, replace "' + q + '" above with a city name instead, e.g. Sao Paulo or Rio de Janeiro';
      hintEl.style.display = "block";
    } else {
      const qUnaccented = stripAccents(q);
      query = query.or(["name.ilike.%"+q+"%","city.ilike.%"+q+"%","city_unaccented.ilike.%"+qUnaccented+"%"].join(","));
    }
  }'''

    new_block = '''  if(q){
    const countryIds = await resolveCountryIds(q);
    if(countryIds.length){
      // The search term matched a real country name exactly - filter by
      // country only, skip the expensive name/city fuzzy search entirely.
      query = query.in("country_id", countryIds);
      hintEl.textContent = 'Tip: for more specific results, replace "' + q + '" above with a city name instead, e.g. Sao Paulo or Rio de Janeiro';
      hintEl.style.display = "block";
      if(countryIds.length === 1){
        const { data: countryRow } = await sb.from("countries").select("currency_code").eq("id", countryIds[0]).maybeSingle();
        const ratesMap = await ensureCurrencyRates();
        updateBudgetLabels(countryRow ? countryRow.currency_code : null, ratesMap);
      } else {
        updateBudgetLabels(null, null);
      }
    } else {
      const qUnaccented = stripAccents(q);
      query = query.or(["name.ilike.%"+q+"%","city.ilike.%"+q+"%","city_unaccented.ilike.%"+qUnaccented+"%"].join(","));
      updateBudgetLabels(null, null);
    }
  } else {
    updateBudgetLabels(null, null);
  }'''

    if old_block not in content:
        print("ERROR: Could not find country-resolution block in runSearch. Helper functions added but NOT hooked in.")
    else:
        content = content.replace(old_block, new_block)
        with open(FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("Done. Budget dropdown now shows real local-currency labels for single-country searches, USD otherwise.")

if content == original:
    print("WARNING: No changes were made at all.")
