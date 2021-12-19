/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s: string): boolean {
    if (s.length % 2 !== 0) return false;

    const open = {
        '(': '(',
        '[': '[',
        '{': '{'
    }

    const close = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    let stack: string[] = [];
    for (let i = 0; i < s.length; i++) {
        let currentValue = s[i];
        if (open.hasOwnProperty(currentValue)) {
            stack.push(currentValue);
        }
        if (close.hasOwnProperty(currentValue)) {
            let popped: string = stack.pop();
            if (popped !== close[currentValue]) {
                return false;
            }
        }
    }

    if (stack.length === 0) {
    return true;
    }
    return false;
}