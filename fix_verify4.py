with open('verify.js', 'r') as f:
    verify_content = f.read()

verify_content = verify_content.replace('classList: { add: ()=>{}, remove: ()=>{}, toggle: ()=>{}, contains: () => false },', 'classList: { add: ()=>{}, remove: ()=>{}, toggle: ()=>{}, contains: () => false }, contains: () => false, children: [], ')

with open('verify.js', 'w') as f:
    f.write(verify_content)
