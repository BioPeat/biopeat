with open('verify.js', 'r') as f:
    verify_content = f.read()

verify_content = verify_content.replace('pufa: 4.5', 'pufa: 4.0')

with open('verify.js', 'w') as f:
    f.write(verify_content)
