# Flask Entra ID SSO

This is a Python Flask web application that integrates with Microsoft Entra ID for Single Sign-On (SSO) authentication using OpenID Connect and OAuth 2.0.

---

## Project Walkthrough
This project demonstrates how to integrate a Python Flask web application with Microsoft Entra ID for Single Sign-On (SSO) authentication using OAuth 2.0, OpenID Connect, and the Microsoft Authentication Library (MSAL).
First, I built a small App using Flask, just a basic login page.
<img width="1507" height="937" alt="1 1-SSO" src="https://github.com/user-attachments/assets/1d75ee7a-3392-4120-b5a4-ba37ed182a3b" />


---


### 1. Flask Login Page

<img width="1505" height="691" alt="1 1-SSO (2)" src="https://github.com/user-attachments/assets/ac17a87c-4ee3-4e39-9b65-7d4b1b82a454" />


The application's landing page. Users can initiate the Microsoft Entra ID authentication process by selecting **Login with Microsoft**.

---

### 2. Azure App Registration

<img width="1898" height="722" alt="1 2-SSO" src="https://github.com/user-attachments/assets/299ae1e3-021c-4017-92ff-8468905a78ad" />


A new application registration is created in Microsoft Entra ID. This establishes trust between the Flask application and Microsoft's identity platform.

---

### 3. Redirect URI Configuration

<img width="1631" height="978" alt="1 3-SSO" src="https://github.com/user-attachments/assets/ad224318-b1ac-466c-83d2-3eef3b607c53" />


The redirect URI is configured during app registration. After successful authentication, Microsoft redirects users back to this URL where the Flask application processes the authorization response. Note that the URL in your terminal is http://127.0.0.1:5000 ->, but here you need to changed to http://localhost:5000/getAToken

---

### 4. Application Registration Overview

<img width="1637" height="642" alt="1 4-SSO" src="https://github.com/user-attachments/assets/f7ddc8c0-2935-4dc6-8a3c-faa125396583" />


Overview page showing the application's Client ID and Tenant ID. These identifiers are used by MSAL to connect the Flask application to the correct Entra ID tenant.

---

### 5. MSAL Configuration in Flask

<img width="1059" height="696" alt="1 5-SSO" src="https://github.com/user-attachments/assets/c7a56306-def6-48b8-9023-fa94d0b96dc8" />

The Flask application imports MSAL and creates a Confidential Client Application using the Client ID, Tenant ID, and Client Secret. This enables secure communication with Microsoft Entra ID.

---

### 6. Login and Authorization Callback Routes

<img width="1306" height="720" alt="1 6-SSO12" src="https://github.com/user-attachments/assets/abec1ac0-881e-4c55-a38c-6a64c00a40cd" />


The `/login` route redirects users to Microsoft for authentication, while the `/getAToken` callback route receives the authorization code and exchanges it for authentication tokens.

---

### 7. Microsoft Sign-In Experience

<img width="1490" height="702" alt="3-SSO" src="https://github.com/user-attachments/assets/c6861e1c-829f-4c49-bfa1-5613b5208bbb" />


Users authenticate through Microsoft's hosted sign-in page, ensuring credentials are never handled directly by the Flask application.

---

### 8. Multi-Factor Authentication (MFA)

<img width="1311" height="667" alt="4-SSO" src="https://github.com/user-attachments/assets/2e46d270-60cf-448f-a5dc-2b212c95364e" />


After entering credentials, users complete Multi-Factor Authentication (MFA). This adds an additional layer of security to the sign-in process.

---

### 9. Logout Flow

<img width="782" height="520" alt="1 6-SSO" src="https://github.com/user-attachments/assets/63517ca3-c8b1-4762-b8ab-54a4e428bda1" />


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
