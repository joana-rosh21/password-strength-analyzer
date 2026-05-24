from pyngrok import ngrok

# 1. Paste your Ngrok Auth Token inside the quotes below:
NGROK_TOKEN = "token"
ngrok.set_auth_token(NGROK_TOKEN)

# 2. Terminate any old background instances of streamlit or ngrok just in case
ngrok.kill()
!pkill streamlit

# 3. Open a tunnel on port 8501 (Streamlit's default port)
public_url = ngrok.connect(8501)
print("👉 CLICK THIS URL TO OPEN YOUR APP:\n", public_url.public_url)

# 4. Start Streamlit in the background
!streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > /dev/null 2>&1 &
