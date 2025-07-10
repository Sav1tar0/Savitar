# 📊 Exam Results Dashboard

A beautiful, responsive webpage to display academic exam results with modern UI and interactive features.

## 🚀 Quick Start

### Method 1: Using Python Server (Recommended)
```bash
python3 run_server.py
```
This will automatically open your browser to view the exam results dashboard.

### Method 2: Direct Browser Opening
Simply double-click on `exam-results.html` or open it directly in your web browser.

## ✨ Features

- **Modern Design**: Beautiful gradient backgrounds and card-based layout
- **Responsive**: Works perfectly on desktop, tablet, and mobile devices
- **Interactive Search**: Search subjects by name or code
- **Grade Filtering**: Filter results by specific grades (A, B, C, D, F)
- **Auto-calculated Statistics**: 
  - Total Credits
  - GPA (Grade Point Average)
  - Overall Percentage
  - Academic Status
- **Print Functionality**: Print-friendly layout for physical copies
- **Real-time Updates**: All calculations update dynamically as you filter

## 🛠️ Customization

### Adding Your Own Data

1. Open `exam-results.html` in a text editor
2. Find the `examResults` array in the JavaScript section (around line 265)
3. Replace the sample data with your actual exam results:

```javascript
const examResults = [
    { 
        code: 'CS101', 
        name: 'Computer Science Fundamentals', 
        credits: 4, 
        marks: 92, 
        grade: 'A', 
        gradePoints: 4.0 
    },
    // Add more subjects here...
];
```

### Updating Student Information

Find the `updateStudentInfo` function call near the end of the JavaScript and uncomment/modify it:

```javascript
updateStudentInfo('Your Name', 'Your ID', '2023-2024', 'Fall 2024');
```

### Customizing Colors

The webpage uses CSS custom properties. You can modify the gradient colors in the CSS section:

- Main background: `#667eea` to `#764ba2`
- Info cards: `#f093fb` to `#f5576c`
- Grade colors: Each grade has its own gradient

### Adding More Subjects

Simply add more objects to the `examResults` array following the same structure:

```javascript
{
    code: 'SUBJECT_CODE',
    name: 'Subject Full Name',
    credits: 3,
    marks: 85,
    grade: 'B',
    gradePoints: 3.0
}
```

## 📊 Grade System

The default grading system used:
- **A**: 90-100 marks, 4.0 grade points
- **B**: 80-89 marks, 3.0 grade points  
- **C**: 70-79 marks, 2.0 grade points
- **D**: 60-69 marks, 1.0 grade points
- **F**: Below 60 marks, 0.0 grade points

### Academic Status Calculation:
- **Excellent**: GPA ≥ 3.5
- **Good**: GPA ≥ 3.0
- **Pass**: GPA ≥ 2.0
- **Fail**: GPA < 2.0

## 🎨 Design Features

- **Gradient Backgrounds**: Modern gradient designs throughout
- **Color-coded Grades**: Each grade has a unique color for easy identification
- **Hover Effects**: Interactive elements with smooth transitions
- **Card Layout**: Information organized in visually appealing cards
- **Mobile-first**: Responsive design that works on all screen sizes

## 🖨️ Printing

Click the "Print Results" button or use your browser's print function (Ctrl+P) to get a clean, printer-friendly version of your results.

## 📱 Browser Compatibility

Works on all modern browsers:
- Chrome
- Firefox
- Safari
- Edge

## 🔧 Technical Details

- **Pure HTML/CSS/JavaScript**: No external dependencies
- **Responsive Grid Layout**: CSS Grid and Flexbox for layout
- **Local Storage Ready**: Can be easily extended to save data locally
- **Print Styles**: Optimized for printing

## 📝 Data Structure

Each exam result should follow this structure:

```javascript
{
    code: string,        // Subject code (e.g., "CS101")
    name: string,        // Full subject name
    credits: number,     // Credit hours for the subject
    marks: number,       // Marks obtained (0-100)
    grade: string,       // Letter grade ("A", "B", "C", "D", "F")
    gradePoints: number  // Grade point value
}
```

## 🚨 Troubleshooting

### Server Won't Start
- Make sure Python 3 is installed
- Check if port 8000 is available
- Try running `python run_server.py` instead of `python3`

### Page Not Loading
- Ensure `exam-results.html` is in the same directory as the server script
- Check your browser's developer console for errors

### Calculations Seem Wrong
- Verify that `gradePoints` match your institution's grading scale
- Ensure `credits` are correctly entered for each subject

## 📞 Support

If you need help customizing the webpage or adding features, you can:
1. Modify the JavaScript code to fit your specific needs
2. Adjust the CSS for different styling
3. Add more subjects to the data array

## 📄 License

This project is open source and free to use for educational purposes.

---

**Happy Learning! 🎓**