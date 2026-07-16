path = "forum.html"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        return '<div id="post-'+p.id+'" style="border-bottom:0.5px solid #F0F3FA;padding:14px 0"><div style="font-weight:600;font-size:14px;color:#0D1F4A">'+p.title+pending+'</div><div style="font-size:12px;color:#7A8BAE;margin:4px 0">'+name+since+' · '+new Date(p.created_at).toLocaleDateString()+'</div><div style="font-size:13px;color:#333;margin-bottom:8px">'+p.content+'</div>'+
          '<div id="repliesList-'+p.id+'" style="margin:8px 0 8px 16px"></div>'+
          '<a href="#" onclick="toggleReplyForm(\\''+p.id+'\\');return false;" style="font-size:12px;color:#1B3A7A;font-weight:600">Reply</a>'+
          '<div id="replyForm-'+p.id+'" style="display:none;margin-top:8px;max-width:520px">'+
            '<textarea id="replyText-'+p.id+'" placeholder="Write a reply..." style="width:100%;padding:10px 14px;border:1px solid #E0E8F5;border-radius:8px;font-size:13px;min-height:60px;font-family:inherit"></textarea>'+
            '<button onclick="submitReply(\\''+p.id+'\\')" style="margin-top:6px;background:#1B3A7A;color:#F5C842;border:none;padding:8px 16px;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer">Submit reply</button>'+
            '<div id="replyStatus-'+p.id+'" style="font-size:12px;margin-top:6px"></div>'+
          '</div>'+
        '</div>';
      }).join('');
      data.forEach(p => loadReplies(p.id));
    }'''

new1 = '''        const topicObj = allTopics.find(t => t.id === p.topic_id);
        const topicPill = topicObj ? '<span style="font-family:sans-serif;font-size:10px;font-weight:700;letter-spacing:0.03em;text-transform:uppercase;background:#EEF3FF;color:#1B3A7A;padding:2px 8px;border-radius:99px;display:inline-block;margin-bottom:4px">'+topicObj.name+'</span><br>' : '';
        const initials = (name || 'M').substring(0,2).toUpperCase();
        return '<div id="post-'+p.id+'" style="background:#fff;border:0.5px solid #E0E8F5;border-radius:12px;padding:16px 18px;margin-bottom:12px"><div style="display:flex;gap:10px;align-items:flex-start"><div style="width:36px;height:36px;border-radius:50%;background:#EEF3FF;color:#1B3A7A;display:flex;align-items:center;justify-content:center;font-family:sans-serif;font-weight:700;font-size:13px;flex-shrink:0">'+initials+'</div><div style="flex:1">'+topicPill+'<div style="display:flex;align-items:baseline;gap:8px;flex-wrap:wrap">'+'<span style="font-family:sans-serif;font-weight:700;font-size:13px;color:#0D1F4A">'+name+'</span><span style="font-family:sans-serif;font-size:11px;color:#9AB0D0">'+since+' · '+new Date(p.created_at).toLocaleDateString()+'</span></div><div style="font-family:sans-serif;font-weight:700;font-size:15px;color:#0D1F4A;margin:6px 0 4px">'+p.title+pending+'</div><div style="font-family:sans-serif;font-size:13px;color:#333;margin-bottom:8px;line-height:1.5">'+p.content+'</div>'+
          '<div id="repliesList-'+p.id+'" style="margin:8px 0 8px 16px"></div>'+
          '<a href="#" onclick="toggleReplyForm(\\''+p.id+'\\');return false;" style="font-family:sans-serif;font-size:12px;color:#1B3A7A;font-weight:700;text-decoration:none">Reply →</a>'+
          '<div id="replyForm-'+p.id+'" style="display:none;margin-top:8px;max-width:520px">'+
            '<textarea id="replyText-'+p.id+'" placeholder="Write a reply..." style="width:100%;padding:10px 14px;border:1px solid #E0E8F5;border-radius:8px;font-size:13px;min-height:60px;font-family:inherit"></textarea>'+
            '<button onclick="submitReply(\\''+p.id+'\\')" style="margin-top:6px;background:#1B3A7A;color:#F5C842;border:none;padding:8px 16px;border-radius:8px;font-size:12px;font-weight:700;cursor:pointer">Submit reply</button>'+
            '<div id="replyStatus-'+p.id+'" style="font-size:12px;margin-top:6px"></div>'+
          '</div></div></div>'+
        '</div>';
      }).join('');
      data2.forEach(p => loadReplies(p.id));
    }'''

c1 = content.count(old1)
if c1 != 1:
    raise SystemExit(f"ABORTED: expected 1 match, found {c1}. No changes made.")
content = content.replace(old1, new1, 1)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Post cards now use the polished card style: avatar circle, topic pill, refined layout.")
