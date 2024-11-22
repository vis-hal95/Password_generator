# Password_generator
### Key Features:

1. **Random Password Generation**: The password is randomly generated based on the specified length.
2. **Customization**: The user can choose to include or exclude specific characters such as uppercase, lowercase, digits, and special symbols.
3. **GUI Interface**: The application uses **Tkinter** to create a graphical user interface.
4. **Security**: The password is generated securely using the `os.urandom()` method (for cryptographic randomness) or `random.choice()` method for non-cryptographic randomness.
5. **Colorful Layout**: The app has a clean, modern, and colorful interface.

![password](https://github.com/vis-hal95/Password_generator/blob/b37f9eb4a0823d8b3dd20e162e45c4b6b7125914/b9cd677a-6a12-4082-9621-8e94c552a04b.jpeg)

### Detailed Explanation:

1. **Main Window Setup**:
    - We create a `Tk()` instance as the main window, set the title to `"Random Password Generator"`, and set a light background color (`#f0f8ff`).
    - The window size is set to `450x350` pixels to ensure that it looks good and fits the content.
2. **Password Generation**:
    - The user specifies the password length in an entry box (`password_length_entry`).
    - When the **Generate Password** button is clicked, the `generate_password()` function is called.
    - The function generates a random password by ensuring that at least one lowercase letter, one uppercase letter, one digit, and one symbol are included.
    - The password is then shuffled to ensure a random order and displayed in the label `password_output`.
      ![password](https://github.com/vis-hal95/Password_generator/blob/b37f9eb4a0823d8b3dd20e162e45c4b6b7125914/e2c43e68-c52c-49b1-b8f2-b5cce7fd4cea.jpeg)
      
3. **Security**:
    - The password is generated using the `random.choice()` method to select characters randomly from different sets (lowercase, uppercase, digits, and symbols).
    - The length of the password is determined by the user's input. A minimum length of 4 is required to ensure that there is at least one character from each category (lowercase, uppercase, digit, and symbol).
4. **Copy to Clipboard**:
    - The app includes a **Copy to Clipboard** button that allows the user to copy the generated password to the clipboard. The `copy_to_clipboard()` function does this, and a confirmation message is shown to the user via `messagebox.showinfo()`.

    ![password](https://github.com/vis-hal95/Password_generator/blob/b37f9eb4a0823d8b3dd20e162e45c4b6b7125914/092a983c-689f-485f-ba13-bd7d53123dc8.jpeg)
   
6. **Colorful Buttons**:
    - The **Generate Password** button is styled with a blue background (`#007bff`), while the **Copy to Clipboard**button has a green background (`#28a745`).
    - The buttons are given a `relief="flat"` style to provide a modern, flat design.
7. **User Guidance**:
    - There is a footer label at the bottom explaining that the password will contain a mix of characters. This helps the user understand the security of the generated password.
    - If the user tries to copy the password without generating one, a warning is displayed using `messagebox.showwarning()`.
8. **Custom Fonts**:
    - The app uses **Helvetica** font for a modern look. The font size is set to `12` for general text and `16` for the heading, making the interface clean and easy to read.

### How the App Works:

1. **Start the App**: When the app starts, a prompt asks the user to enter the desired password length in an entry box.
2. **Generate Password**: The user clicks the **Generate Password** button, and the password is displayed below the button.
3. **Copy Password**: After generating the password, the user can click the **Copy to Clipboard** button to copy the password for use elsewhere.
4. **User Feedback**: If the user tries to generate a password with a length less than 4, a warning is shown.


### Example Output:

1. **Start Screen**: The user sees a clean screen asking for the password length.
2. **Generated Password**: After clicking "Generate Password", a random password appears, including a mix of characters.
3. **Copy Confirmation**: When the user clicks "Copy to Clipboard", a popup appears saying the password was copied.
