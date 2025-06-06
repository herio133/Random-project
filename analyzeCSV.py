import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

def analyze_csv_file(file_path, text_area):
    """Read and analyze a CSV file"""
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        
        # Clear previous results
        text_area.delete(1.0, tk.END)
        
        # Show basic info
        text_area.insert(tk.END, f"File loaded successfully!\n")
        text_area.insert(tk.END, f"Number of rows: {len(data)}\n")
        text_area.insert(tk.END, f"Number of columns: {len(data.columns)}\n\n")
        
        # Show column names
        text_area.insert(tk.END, "Column names:\n")
        for i, col in enumerate(data.columns, 1):
            text_area.insert(tk.END, f"{i}. {col}\n")
        text_area.insert(tk.END, "\n")
        
        # Find number columns only
        number_columns = []
        for col in data.columns:
            if data[col].dtype in ['int64', 'float64']:
                number_columns.append(col)
        
        if len(number_columns) == 0:
            text_area.insert(tk.END, "No number columns found to analyze.\n")
            return
        
        # Analyze each number column
        text_area.insert(tk.END, "Analysis of number columns:\n")
        text_area.insert(tk.END, "=" * 40 + "\n")
        
        for col in number_columns:
            text_area.insert(tk.END, f"\nColumn: {col}\n")
            text_area.insert(tk.END, f"Average: {data[col].mean():.2f}\n")
            text_area.insert(tk.END, f"Highest: {data[col].max()}\n")
            text_area.insert(tk.END, f"Lowest: {data[col].min()}\n")
            text_area.insert(tk.END, f"Middle value: {data[col].median():.2f}\n")
            
    except FileNotFoundError:
        messagebox.showerror("File Error", "The file was not found. Please check if the file exists.")
    except pd.errors.EmptyDataError:
        messagebox.showerror("Empty File", "The CSV file is empty or has no data to analyze.")
    except pd.errors.ParserError:
        messagebox.showerror("Format Error", "The file format is incorrect. Please ensure it's a valid CSV file.")
    except PermissionError:
        messagebox.showerror("Permission Error", "Cannot access the file. It might be open in another program.")
    except Exception as error:
        messagebox.showerror("Unexpected Error", f"Something went wrong:\n{str(error)}\n\nPlease try a different file.")

def choose_file():
    """Let user pick a CSV file with better validation"""
    # Show file dialog with multiple file type options
    file_path = filedialog.askopenfilename(
        title="Select a CSV file to analyze",
        filetypes=[
            ("CSV files", "*.csv"),
            ("Text files", "*.txt"),
            ("All files", "*.*")
        ],
        initialdir=".",  # Start in current directory
    )
    
    # Check if user actually selected a file
    if not file_path:
        return  # User cancelled, do nothing
    
    # Validate file extension
    if not file_path.lower().endswith(('.csv', '.txt')):
        response = messagebox.askyesno(
            "File Type Warning", 
            f"The selected file doesn't appear to be a CSV file.\n\nFile: {file_path.split('/')[-1]}\n\nDo you want to try analyzing it anyway?"
        )
        if not response:
            return
    
    # Show loading message for large files
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, "Loading file, please wait...\n")
    window.update()  # Refresh the display
    
    # Try to analyze the file
    try:
        analyze_csv_file(file_path, results_text)
        # Show success message in status
        window.title(f"Simple CSV Analyzer - {file_path.split('/')[-1]}")
    except Exception:
        # If analysis fails, the error is already handled in analyze_csv_file
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "Failed to analyze file. Please try another file.")

def save_results():
    """Save analysis results to a text file"""
    if not results_text.get(1.0, tk.END).strip():
        messagebox.showwarning("No Results", "No analysis results to save!")
        return
    
    file_path = filedialog.asksaveasfilename(
        title="Save analysis results",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if file_path:
        try:
            with open(file_path, 'w') as f:
                f.write(results_text.get(1.0, tk.END))
            messagebox.showinfo("Success", f"Results saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save file:\n{e}")

def clear_results():
    """Clear the results area"""
    if results_text.get(1.0, tk.END).strip():
        if messagebox.askyesno("Clear Results", "Are you sure you want to clear all results?"):
            results_text.delete(1.0, tk.END)
            window.title("Simple CSV Analyzer")

# Create the main window
window = tk.Tk()
window.title("Simple CSV Analyzer")
window.geometry("750x520")
window.minsize(600, 400)
window.configure(bg="#f4f6fa")

# Style configuration
button_style = {
    "font": ("Segoe UI", 11, "bold"),
    "width": 16,
    "height": 2,
    "bd": 0,
    "relief": tk.FLAT,
    "activebackground": "#e0e7ef",
    "cursor": "hand2"
}

# Create a frame for buttons
button_frame = tk.Frame(window, bg="#f4f6fa")
button_frame.pack(pady=18)

choose_button = tk.Button(
    button_frame,
    text="📂  Choose CSV File",
    command=choose_file,
    bg="#4f8cff",
    fg="white",
    activeforeground="#222",
    **button_style
)
choose_button.pack(side=tk.LEFT, padx=8)

save_button = tk.Button(
    button_frame,
    text="💾  Save Results",
    command=save_results,
    bg="#43d19e",
    fg="white",
    activeforeground="#222",
    **button_style
)
save_button.pack(side=tk.LEFT, padx=8)

clear_button = tk.Button(
    button_frame,
    text="🗑️  Clear",
    command=clear_results,
    bg="#ff6b6b",
    fg="white",
    activeforeground="#222",
    **button_style
)
clear_button.pack(side=tk.LEFT, padx=8)

# Add text area to show results
results_text = scrolledtext.ScrolledText(
    window,
    width=85,
    height=24,
    font=("Consolas", 11),
    bg="#fafdff",
    fg="#222",
    bd=1,
    relief=tk.FLAT,
    padx=10,
    pady=8,
    wrap=tk.WORD
)
results_text.pack(padx=24, pady=12, fill=tk.BOTH, expand=True)

# Start the program
window.mainloop()
