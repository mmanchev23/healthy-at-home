import axios from 'axios';
import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input, Spinner } from "reactstrap";

const Register = () => {
    const [username, setUsername] = useState("");
    const [password1, setPassword1] = useState("");
    const [password2, setPassword2] = useState("");
    const [loading, setLoading] = useState(false);
    const history = useHistory();

    const handleRegister = async e => {
        e.preventDefault();
        setLoading(true);
    
        await axios.post("http://127.0.0.1:8000/api/v1/auth/register/", { username, password1, password2 })
        .then(response => {
            sessionStorage.setItem("key", response.data.key);
            setLoading(false);
        
            history.push({
                pathname: "/",
                state: {
                    message: "You have registered successfully!"
                }
            });
            window.location.reload();
        })
        .catch(() => {
            if (!username) {
                toast.error("Username field can not be empty!", {
                    transition: Slide,
                    position: "top-right",
                    autoClose: 5000
                })
                setLoading(false);
            } else if (username.length < 8) {
                toast.error("Username cannot be less than 8 characters long!", {
                    transition: Slide,
                    position: "top-right",
                    autoClose: 5000
                })
                setLoading(false);
            } else if (/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/.exec(password1)) {
                toast.error("Password 1 format not valid!\nValid password contains atleast one upper/lower-case character, digit and special characters!", {
                    transition: Slide,
                    position: "top-right",
                    autoClose: 5000
                })
                setLoading(false);
            } else if (/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/.exec(password2)) {
                toast.error("Password 2 format not valid!\nValid password contains atleast one upper/lower-case character, digit and special characters!", {
                    transition: Slide,
                    position: "top-right",
                    autoClose: 5000
                })
                setLoading(false);
            } else if (password1 !== password2) {
                toast.error("Passwords should match!", {
                    transition: Slide,
                    position: "top-right",
                    autoClose: 5000
                })
                setLoading(false);
            }
        })
      }

    const goBack = (e) => {
        e.preventDefault();
        history.goBack();
    }

    return (
        <Modal isOpen={true}>
            <ModalHeader>Register</ModalHeader>
            <ModalBody>
                <Form>
                    <FormGroup>
                        <Label>Username</Label>
                        <Input type="text" onChange={(e) => setUsername(e.target.value)} placeholder="Enter username"/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Password</Label>
                        <Input type="password" onChange={(e) => setPassword1(e.target.value)} placeholder="Enter password"/>
                    </FormGroup>
                    <FormGroup>
                        <Label>Confirm Password</Label>
                        <Input type="password" onChange={(e) => setPassword2(e.target.value)} placeholder="Confirm password"/>
                    </FormGroup>
                </Form>
            </ModalBody>
            <ModalFooter>
                <Button color="success" type="submit" onClick={handleRegister} disabled={!(username && password1 && password2)}>{loading ? <Spinner color="primary"/> : "Register"}</Button>
                <Button color="danger" type="submit" onClick={goBack}> No, bring me back </Button>
                <ToastContainer/>
            </ModalFooter>
        </Modal>
    );
}

export default Register;