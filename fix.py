with open('trace-ive.html', 'r', encoding='utf-8') as f:
    content = f.read()
old = '    const res = await fetch(`${SUPABASE_URL}/rest/v1/submissions?status=eq.pending&order=created_at.desc`, {\n      headers: { \'apikey\': SUPABASE_ANON_KEY, \'Authorization\': `Bearer ${SUPABASE_ANON_KEY}` }\n    });\n    const data = await res.json();\n    const badge = document.getElementById(\'pending-count-badge\');\n    if (badge) badge.textContent = data.length + \'件\';\n    const list = document.getElementById(\'pending-list\');\n    if (!data.length) {'
if old in content:
    print('found')
else:
    print('not found')
