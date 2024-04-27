import pyperclip
import keyboard
import tkinter as tk

from openai import OpenAI

def clipGpt(file_api_key, options):
    client = OpenAI(api_key=file_api_key) #

    # Save the original clipboard content
    original_content = pyperclip.paste()

    def clipboard_changed():
        print("clipboard_changed()")

        global original_content
        new_content = pyperclip.paste()

        # Show the popup window
        root = tk.Tk()
        root.title("ClipGpt")

        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x = int((screen_width - root.winfo_reqwidth()) / 2)
        y = int((screen_height - root.winfo_reqheight()) / 2)

        # Set the window size to 300x200 pixels
        root.geometry("600x400")

        # Set the window position to the center of the screen
        root.geometry(f"+{x}+{y}")
        root.withdraw()

        # Create a listbox with the options
        options = ["Translate clipboard to english", "Rewrite the text in good english"]
        listbox = tk.Listbox(root)
        listbox.pack(fill=tk.BOTH, expand=True)

        for option in options:
            listbox.insert(tk.END, option)

        def exit_window():
            root.destroy()

        text_widget = tk.Text(root, height=10, width=50)
        text_widget.pack(fill=tk.BOTH, expand=True)
                
        # Create a button to send the selected option to ChatGPT
        def send_option():
            # Get the selected option
            selected_option = listbox.get(listbox.curselection())

            # Exchange the clipboard content with a predefined value
            pyperclip.copy("Predefined value")
            print("Clipboard content exchanged with predefined value")

            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": selected_option + ":" + new_content}
                ]
                )
            print(completion.choices[0].message)
            print("Response from ChatGPT:", completion.choices[0].message.content)

            text_widget.insert(tk.END, completion.choices[0].message.content)
            text_widget.see(tk.END)

            pyperclip.copy(completion.choices[0].message.content)

        btn_heigth = 2
        btn_width = 20

        button = tk.Button(root, text="Send to ChatGPT", height=btn_heigth, width=btn_width, command=send_option)
        button.pack()

        exit_button = tk.Button(root, text="Exit", height=btn_heigth, width=btn_width, command=exit_window)
        exit_button.pack()

        # Show the popup window
        root.deiconify()

        root.attributes('-topmost', 1)  # Bring the window to the foreground

        # Run the main event loop
        root.mainloop()
            
    # Listen for the key combination Ctrl+Shift+O
    keyboard.add_hotkey(options["hotkey"], clipboard_changed)