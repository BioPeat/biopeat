with open('verify.js', 'r') as f:
    verify_content = f.read()

verify_content = verify_content.replace('vm.createContext(sandbox);', 'sandbox.requestAnimationFrame = sandbox.window.requestAnimationFrame; vm.createContext(sandbox);')

with open('verify.js', 'w') as f:
    f.write(verify_content)
