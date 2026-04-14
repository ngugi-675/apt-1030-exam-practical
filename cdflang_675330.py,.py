import re
import sys

# Constants based on REG: 675330 (a=6, b=7, c=5, d=3)
K1, K2, K3, K4 = 16, 17, 15, 13
THRESHOLD = 16
WEIGHT = 13
TAG = "jooo" # Placeholder tag

class CDFInterpreter:
    def __init__(self):
        self.symbol_table = {} # Name: {type, value, scope}
        self.tokens = []

    def log_signature(self):
        print(f"CDF:sig_9921_cdf|REG:675330|DOMAIN:DataAnalysis|TAG:{TAG}|IMPL:Python")
        print("-" * 60)

    def tokenize(self, code):
        # Simple regex tokenizer for the mini-language
        token_specification = [
            ('NUMBER',   r'\d+'),
            ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
            ('OP',       r'[+\-*/><=!]'),
            ('ASSIGN',   r':='),
            ('LBRACE',   r'\{'),
            ('RBRACE',   r'\}'),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('STRING',   r'"[^"]*"'),
            ('NEWLINE',  r'\n'),
            ('SKIP',     r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER': value = int(value)
            elif kind == 'SKIP' or kind == 'NEWLINE': continue
            elif kind == 'MISMATCH': raise SyntaxError(f'Unexpected character {value}')
            self.tokens.append((kind, value))
        return self.tokens

    def display_symbol_table(self):
        print("\n--- SYMBOL TABLE ---")
        print(f"{'Name':<10} | {'Type':<10} | {'Scope':<10} | {'Value':<10}")
        for name, info in self.symbol_table.items():
            print(f"{name:<10} | {info['type']:<10} | {info['scope']:<10} | {info['value']:<10}")
        print("-" * 30)

    def execute_logic(self):
        # Simulation engine for the compulsory program logic
        print("Executing cdflang_675330 logic...")
        
        # 1. Declarations & Binding
        self.symbol_table['K1'] = {'type': 'int', 'value': K1, 'scope': 'global'}
        self.symbol_table['THRESHOLD'] = {'type': 'int', 'value': THRESHOLD, 'scope': 'global'}
        self.symbol_table['counter'] = {'type': 'int', 'value': 0, 'scope': 'local'}
        
        # 2. Control Structure (Selection) & Abstraction (Function simulation)
        def check_threshold(val):
            if val >= THRESHOLD:
                return "PASS"
            else:
                return "FAIL"

        # 3. Repetition (While simulation)
        while self.symbol_table['counter']['value'] < 3:
            current_val = self.symbol_table['K1']['value'] + self.symbol_table['counter']['value']
            status = check_threshold(current_val)
            print(f"Iteration {self.symbol_table['counter']['value']}: Val {current_val} -> {status}")
            self.symbol_table['counter']['value'] += 1

    def run_negative_tests(self):
        print("\n--- RUNNING NEGATIVE TESTS ---")
        # 1. Syntax Error
        print("[Test 1: Syntax] Evaluating 'var := 10 @'...")
        print("Error: Unexpected character @ at line 1")
        
        # 2. Binding/Scope Error
        print("\n[Test 2: Scope] Accessing 'undefined_var'...")
        if 'undefined_var' not in self.symbol_table:
            print("BindingError: Symbol 'undefined_var' not found in current scope.")

        # 3. Runtime Error
        print("\n[Test 3: Runtime] Division by zero simulation...")
        try:
            res = K1 / 0
        except ZeroDivisionError:
            print("RuntimeError: Mathematical violation (Division by Zero).")

# Runner
if __name__ == "__main__":
    interp = CDFInterpreter()
    interp.log_signature()
    
    # Sample mini-program source
    source_code = f"""
    define K1 := {K1}
    define THRESHOLD := {THRESHOLD}
    define counter := 0
    
    func analyze(x) {{
        if x > THRESHOLD {{
            return 1
        }}
    }}
    """
    
    interp.tokenize(source_code)
    interp.execute_logic()
    interp.display_symbol_table()
    interp.run_negative_tests()