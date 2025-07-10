#!/usr/bin/env python3
"""
Simple HTTP Server for Exam Results Dashboard
Run this script to serve the exam-results.html file locally
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def run_server():
    # Configuration
    PORT = 8000
    HOST = 'localhost'
    
    # Check if the HTML file exists
    html_file = Path('exam-results.html')
    if not html_file.exists():
        print("❌ Error: exam-results.html not found!")
        print("Please make sure the exam-results.html file is in the same directory.")
        sys.exit(1)
    
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Create server
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer((HOST, PORT), handler) as httpd:
            print("📊 Exam Results Dashboard Server")
            print("=" * 40)
            print(f"🌐 Server running at: http://{HOST}:{PORT}")
            print(f"📄 Serving: {html_file.absolute()}")
            print("=" * 40)
            print("📋 Instructions:")
            print(f"   1. Open your browser and go to: http://{HOST}:{PORT}/exam-results.html")
            print("   2. Or simply wait - the page will open automatically!")
            print("   3. Press Ctrl+C to stop the server")
            print("=" * 40)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://{HOST}:{PORT}/exam-results.html')
                print("🚀 Opening browser automatically...")
            except Exception as e:
                print(f"⚠️  Could not open browser automatically: {e}")
                print(f"   Please manually open: http://{HOST}:{PORT}/exam-results.html")
            
            print("\n✅ Server started successfully! Press Ctrl+C to stop.")
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user.")
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ Error: Port {PORT} is already in use!")
            print("   Try closing other applications or wait a moment and try again.")
            print(f"   Or manually open exam-results.html in your browser.")
        else:
            print(f"❌ Error starting server: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    run_server()