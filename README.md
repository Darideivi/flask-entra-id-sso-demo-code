# Flask Entra ID SSO

This is a Python Flask web application that integrates with Microsoft Entra ID for Single Sign-On (SSO) authentication using OpenID Connect and OAuth 2.0.

---

## Project Walkthrough
This project demonstrates how to integrate a Python Flask web application with Microsoft Entra ID for Single Sign-On (SSO) authentication using OAuth 2.0, OpenID Connect, and the Microsoft Authentication Library (MSAL).
First, I built a small App using Flask, just a basic login page.
<img width="700" alt="App_start" src="https://github.com/user-attachments/assets/efbbfa56-3544-4673-ae07-73999460e184" />

---


### 1. Flask Login Page

<img width="700" alt="1 1-SSO (2)" src="https://github.com/user-attachments/assets/488c9095-a0d4-4410-9cd0-e84e3192f866" />

The application's landing page. Users can initiate the Microsoft Entra ID authentication process by selecting **Login with Microsoft**.

---

### 2. Azure App Registration

<img width="708" alt="1 2-SSO" src="https://github.com/user-attachments/assets/d482988b-8821-4b9d-a613-e2f658982081" />

A new application registration is created in Microsoft Entra ID. This establishes trust between the Flask application and Microsoft's identity platform.

---

### 3. Redirect URI Configuration

<img width="1000" alt="1 3-SSO" src="https://github.com/user-attachments/assets/49f1ce66-16e4-4305-8207-e571bde6b75b" />

The redirect URI is configured during app registration. After successful authentication, Microsoft redirects users back to this URL where the Flask application processes the authorization response. Note that the URL in your terminal is http://127.0.0.1:5000 ->, but here you need to changed to http://localhost:5000/getAToken

---

### 4. Application Registration Overview

<img width="1337" alt="1 4-SSO" src="https://github.com/user-attachments/assets/9bf6771a-a866-4013-bcf2-265825b4ae1f" />

Overview page showing the application's Client ID and Tenant ID. These identifiers are used by MSAL to connect the Flask application to the correct Entra ID tenant.

---

### 5. MSAL Configuration in Flask

<img width="759" alt="1 5-SSO" src="https://github.com/user-attachments/assets/21dec86e-3f47-4ae6-90d7-c55c45c628b7" />

The Flask application imports MSAL and creates a Confidential Client Application using the Client ID, Tenant ID, and Client Secret. This enables secure communication with Microsoft Entra ID.

---

### 6. Login and Authorization Callback Routes

<img width="1006" alt="1 6-SSO12" src="https://github.com/user-attachments/assets/38f31f7d-aef8-45a8-b380-76984c49b291" />

The `/login` route redirects users to Microsoft for authentication, while the `/getAToken` callback route receives the authorization code and exchanges it for authentication tokens.

---

### 7. Microsoft Sign-In Experience

<img width="1190" alt="3-SSO" src="https://github.com/user-attachments/assets/ee550b65-0e65-47e9-a8f0-3661ad5980fd" />

Users authenticate through Microsoft's hosted sign-in page, ensuring credentials are never handled directly by the Flask application.

---

### 8. Multi-Factor Authentication (MFA)

<img width="1011" alt="4-SSO" src="https://github.com/user-attachments/assets/cf112320-e521-4a29-a4c0-1d08401da730" />

After entering credentials, users complete Multi-Factor Authentication (MFA). This adds an additional layer of security to the sign-in process.

---

### 9. Logout Flow

<img width="782" alt="1 6-SSO" src="https://github.com/user-attachments/assets/88e1c3b7-8b47-4a9c-b20a-cf4a7335386f" />

When users sign out, the Flask session is cleared and Microsoft terminates the authenticated session, completing the logout process.

---
## Authentication Flow

```text
User
  ↓
Flask Application
  ↓
MSAL Library
  ↓
Microsoft Entra ID
  ↓
Authorization Code
  ↓
Access / ID Tokens
  ↓
User Session Created
  ↓
Authenticated User
```

This project uses the OAuth 2.0 Authorization Code Flow with OpenID Connect (OIDC). Users authenticate through Microsoft Entra ID, and the application uses MSAL to securely exchange authorization codes for tokens and create authenticated sessions.

---

## Key Takeaways

Through this project, I gained hands-on experience with:

- Single Sign-On (SSO) using Microsoft Entra ID
- OAuth 2.0 and OpenID Connect (OIDC)
- Application registration and configuration in Microsoft Entra ID
- Redirect URIs, Client IDs, Tenant IDs, and Client Secrets
- Microsoft Authentication Library (MSAL) integration
- User session creation and management in Flask
- Authentication versus authorization concepts
- Troubleshooting SSO issues such as redirect URI mismatches and authentication failures
- Enterprise identity and access management fundamentals
- Secure authentication without storing user credentials locally
```
