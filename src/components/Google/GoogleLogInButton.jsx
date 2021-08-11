import React from 'react';
import axios from "axios";
import { useHistory } from "react-router-dom";
import GoogleLogin from 'react-google-login';

const GoogleLogInButton = () => {
  const history = useHistory();

  const googleLogin = async response => {
    await axios.post("http://127.0.0.1:8000/api/v1/auth/google/", { access_token: response.accessToken })
    .then(response => {
      sessionStorage.setItem("key", response.data.key);

      history.push({
        pathname: "/",
        state: {
          message: "You have logged in successfully!"
        }
      });

      window.location.reload();
    });
  }

  return (
    <div className="App">
      <GoogleLogin
        clientId="910309434618-b66m6bjnvg561lc26lk84dt5lskq77t3.apps.googleusercontent.com"
        buttonText="Log in with Google"
        onSuccess={googleLogin}
        onFailure={googleLogin}
        cookiePolicy={'single_host_origin'}
      />
    </div>
  );
}

export default GoogleLogInButton;