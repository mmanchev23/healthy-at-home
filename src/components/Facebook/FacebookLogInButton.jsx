import React from 'react';
import axios from "axios";
import { useHistory } from "react-router-dom";
import FacebookLogin from 'react-facebook-login';

const FacebookLogInButton = () => {
  const history = useHistory();

  const facebookLogin = async response => {
    await axios.post("http://127.0.0.1:8000/api/v1/auth/facebook/", { access_token: response.accessToken })
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
    <FacebookLogin
      textButton="Login with Facebook"
      appId= "243010007282017"
      fields="name,email,picture"
      callback={facebookLogin}
    />
  </div>
  );
}

export default FacebookLogInButton;