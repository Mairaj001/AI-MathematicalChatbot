import tkinter as tk
from tkinter import scrolledtext
import sympy as sp

operations = {
    '1': 'Simplify',
    '2': 'Differentiate',
    '3': 'Integrate',
    '4': 'Solve',
    '5': 'Matrix Multiplication',
    '6': 'Matrix Addition'
    
}

def perform_operation(operation_code, expression):
    try:
        print(operation_code,expression)
        if ":" in expression:  
            operation, matrices_expr = expression.split(":", 1)
            if operation_code == '5':
                matrices = [sp.Matrix(eval(matrix)) for matrix in matrices_expr.split("::")]
                matrix1, matrix2 = matrices
                result = matrix1 * matrix2
                return result
            elif operation_code == '6':
                matrices = [sp.Matrix(eval(matrix)) for matrix in matrices_expr.split("::")]
                matrix1, matrix2 = matrices
                result = matrix1 + matrix2
                return result
            elif operation_code == '4':  # For solving equations
                expressions = [sp.sympify(expr.strip()) for expr in matrices_expr.split(",")]
                print(expressions,"expression")  # Debugging print
                result = sp.solve(expressions)
                print(result)  # Debugging print
                return result
        else:  
            x = sp.symbols('x')
            expression = sp.sympify(expression)
            if operation_code == '1':
                return sp.simplify(expression)
            elif operation_code == '2':
                return sp.diff(expression, x)
            elif operation_code == '3':
                return sp.integrate(expression, x)
            elif operation_code == '4':
                return sp.solve(expression, x)
    except (sp.SympifyError, TypeError, ValueError) as e:
        return "Invalid input or operation."
def send_message():
    user_input = input_field.get()
    arr = ['exit', 'quit', 'bye']
    if user_input.lower() in arr:
        chat_box.insert(tk.END, "You: " + user_input + "\n", "user")
        chat_box.insert(tk.END, "AlgeBot: Goodbye!\n", "bot")
        input_field.delete(0, tk.END)
        input_field.config(state=tk.DISABLED)
    else:
        if not user_input.strip():
            chat_box.insert(tk.END, "AlgeBot: Hi there! I am your mathematical assistant. You can ask me to solve mathematical problems.\n", "bot")
        else:
            split_input = user_input.split(':')  
            print(split_input)  # Print the split input for debugging
            if len(split_input) == 2:  
                operation_code, expression = split_input
                result = perform_operation(operation_code.strip(), expression.strip())
                if result is not None:
                    chat_box.insert(tk.END, "You: " + user_input + "\n", "user")
                    chat_box.insert(tk.END, "AlgeBot: " + str(result) + "\n", "bot")
                else:
                    chat_box.insert(tk.END, "AlgeBot: Unable to perform the operation.\n", "bot")
            elif len(split_input) == 1 and split_input[0].strip().startswith('4'):  # Check if operation code starts with '4'
                expression = user_input.split(',')[0].strip()  # Split using ',' for solving equations
                result = perform_operation('4', expression)  # Pass '4' as the operation code
                if result is not None:
                    chat_box.insert(tk.END, "You: " + user_input + "\n", "user")
                    chat_box.insert(tk.END, "AlgeBot: " + str(result) + "\n", "bot")
                else:
                    chat_box.insert(tk.END, "AlgeBot: Unable to perform the operation.\n", "bot")
            else:
                chat_box.insert(tk.END, "AlgeBot: Invalid input format. Please use 'operation: expression'.\n", "bot")
        
        chat_box.insert(tk.END, "\n")
        input_field.delete(0, tk.END)
root = tk.Tk()
root.title("AlgeBot Chat")
root.geometry("1020x500")
root.configure(bg="#153448")
root.resizable(False, False)

left_frame = tk.Frame(root, bg="#153448")
left_frame.pack(fill=tk.BOTH, side=tk.LEFT)

bot_name_label = tk.Label(left_frame, text="AlgeBot", font=("Arial", 20, "bold"), bg="#153448", fg="white")
bot_name_label.pack(pady=(20, 10))

bot_functionality_label = tk.Label(left_frame, text="Symbolic Computation Chatbot", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label.pack()

bot_functionality_label1 = tk.Label(left_frame, text="1:Simplify", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label1.pack()

bot_functionality_label2 = tk.Label(left_frame, text="2:Differentiate", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label2.pack()

bot_functionality_label3 = tk.Label(left_frame, text="3:Integrate", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label3.pack()

bot_functionality_label4 = tk.Label(left_frame, text="4:Solve", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label4.pack()


bot_functionality_label5 = tk.Label(left_frame, text="5:Matrix Multiplication", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label5.pack()


bot_functionality_label6 = tk.Label(left_frame, text="6:Matrix Addition", font=("Arial", 12), bg="#153448", fg="white")
bot_functionality_label6.pack()
input_field = tk.Entry(left_frame, width=20, font=("Arial", 12))
input_field.pack(side=tk.LEFT, padx=(10, 0), pady=10)

send_button = tk.Button(left_frame, text="Send", width=10, font=("Arial", 12), command=send_message, bg="orange", fg="white")
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=10)

right_frame = tk.Frame(root, bg="#153448")
right_frame.pack(expand=True, fill=tk.BOTH)

chat_box = scrolledtext.ScrolledText(right_frame, width=50, height=20, wrap=tk.WORD, bg="#153448", fg="white")
chat_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
chat_box.tag_configure("bot", foreground="white", font=("Arial", 12))
chat_box.tag_configure("user", foreground="white", font=("Arial", 12))


send_message()

root.mainloop()
