@echo off
echo 🚀 Uploading Data Cleaning Tool to GitHub...
echo.

echo 📋 Checking Git installation...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed or not in PATH
    echo 📥 Please install Git from: https://git-scm.com/
    echo 📖 Then run this script again
    pause
    exit /b 1
)

echo ✅ Git is installed
echo.

echo 🔧 Initializing Git repository...
git init
if %errorlevel% neq 0 (
    echo ❌ Failed to initialize Git repository
    pause
    exit /b 1
)

echo ✅ Git repository initialized
echo.

echo 🔗 Adding remote repository...
git remote add origin https://github.com/aboazab1/Data-Cleaning-Tool-AbO-Azab.git
if %errorlevel% neq 0 (
    echo ⚠️  Remote already exists, updating...
    git remote set-url origin https://github.com/aboazab1/Data-Cleaning-Tool-AbO-Azab.git
)

echo ✅ Remote repository configured
echo.

echo 📁 Adding all files to Git...
git add .
if %errorlevel% neq 0 (
    echo ❌ Failed to add files
    pause
    exit /b 1
)

echo ✅ Files added to Git
echo.

echo 💾 Committing files...
git commit -m "Initial commit: Data Cleaning Tool with GUI

Features:
- Automatic delimiter detection
- Data cleaning and type conversion  
- Excel and CSV export
- User-friendly GUI
- Bilingual documentation (Arabic/English)
- Professional README with developer info

Developer: Abdelrahman Adel Alazab
Email: abdelrahmanalazab4@gmail.com
Phone: +966 57 353 2943
Location: Riyadh, Saudi Arabia

🎯 Building tomorrow's solutions with today's technology"
if %errorlevel% neq 0 (
    echo ❌ Failed to commit files
    pause
    exit /b 1
)

echo ✅ Files committed successfully
echo.

echo 🚀 Pushing to GitHub...
git branch -M main
git push -u origin main
if %errorlevel% neq 0 (
    echo ❌ Failed to push to GitHub
    echo 💡 You may need to authenticate with GitHub
    echo 📖 Check the GITHUB_UPLOAD_GUIDE.md for detailed instructions
    pause
    exit /b 1
)

echo.
echo 🎉 SUCCESS! Project uploaded to GitHub
echo 🌐 Repository: https://github.com/aboazab1/Data-Cleaning-Tool-AbO-Azab
echo.
echo 📋 Next steps:
echo 1. Visit your repository on GitHub
echo 2. Add repository description and topics
echo 3. Enable Issues and Discussions
echo 4. Create your first release
echo.
echo 📖 For detailed instructions, see GITHUB_UPLOAD_GUIDE.md
echo.
pause
