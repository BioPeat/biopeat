with open('verify.js', 'r') as f:
    verify_content = f.read()

verify_content = verify_content.replace('vm.createContext(sandbox);', 'sandbox.performance = { now: () => Date.now() }; vm.createContext(sandbox);')

with open('verify.js', 'w') as f:
    f.write(verify_content)
