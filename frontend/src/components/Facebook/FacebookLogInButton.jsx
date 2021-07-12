import React from 'react';
import axios from "axios";
import { useHistory } from "react-router-dom";
import FacebookLogin from 'react-facebook-login';

const FacebookLogInButton = () => {
  const history = useHistory();

  const facebookLogin = async response => {
    await axios.post("https://healthy-at-home2.herokuapp.com/api/facebook/", { access_token: response.accessToken })
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