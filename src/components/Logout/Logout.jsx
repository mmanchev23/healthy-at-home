import React from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import { Button, Form, Modal, ModalHeader, ModalFooter } from "reactstrap";

const Logout = () => {
    const history = useHistory();

    const handleLogout = (e) => {
        e.preventDefault();
        sessionStorage.clear();
        
        toast.success("You have logged out successfully!", {
            transition: Slide,
            position: "top-right",
            autoClose: 2500
        });
    
        setInterval(() => {
            history.push("/");
            window.location.reload();
        }, 2500);
    }

    const goBack = (e) => {
        e.preventDefault();
        history.goBack();
    }

    return(
        <Modal isOpen={true}>
            <Form>
                <ModalHeader>Log out?</ModalHeader>
                <ModalFooter>
                    <Button color="success" type="submit" onClick={handleLogout}>Yes, log me out</Button>
                    <Button color="danger" type="submit" onClick={goBack}>No, bring me back</Button>
                    <ToastContainer/>
                </ModalFooter>
            </Form>
        </Modal>
    );
}

export default Logout;