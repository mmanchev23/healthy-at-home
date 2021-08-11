import axios from 'axios';
import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
// import GoogleLogInButton from '../Google/GoogleLogInButton';
// import FacebookLogInButton from '../Facebook/FacebookLogInButton';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input } from "reactstrap";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  // const [loading, setLoading] = useState(false);
  const history = useHistory();

  const handleLogin = async e => {
    e.preventDefault();
    // setLoading(true);

    await axios.post("http://127.0.0.1:8000/api/login/", { username, password })
    .then(response => {
      sessionStorage.setItem("key", response.data.key);
      // setLoading(false);

      toast.success("You have logged in successfully!", {
        transition: Slide,
        position: "top-right",
        autoClose: 5000
      });

      setInterval(() => {
        history.push("/");
        window.location.reload();
      }, 5000);
    })
    .catch(error => {
      console.log(error);
      
      toast.error("Invalid credentials!", {
        transition: Slide,
        position: "top-right",
        autoClose: 5000
      })
    });
  }

  const goBack = (e) => {
      e.preventDefault();
      history.goBack();
  }

  return(
    <div>
      <Modal isOpen={true}>
        <Form>
          <ModalHeader>Log in</ModalHeader>
          <ModalBody>
              <FormGroup>
                <Label>Username</Label>
                <Input type="text" onChange={(e) => setUsername(e.target.value)} placeholder="Enter username"/>
              </FormGroup>
              <FormGroup>
                <Label>Password</Label>
                <Input type="password" onChange={(e) => setPassword(e.target.value)}placeholder="Enter password"/>
              </FormGroup>
          </ModalBody>
          <ModalFooter>
            {/* <FacebookLogInButton/>
            <GoogleLogInButton/> */}
            <Button color="success" type="submit" onClick={handleLogin} disabled={!(username && password)}>Log in</Button>
            <Button color="danger" type="submit" onClick={goBack}>No, bring me back</Button>
            <ToastContainer/>
          </ModalFooter>
        </Form>
      </Modal>
    </div>
  )
}

export default Login;