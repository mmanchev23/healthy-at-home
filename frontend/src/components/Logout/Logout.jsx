import React from 'react';
import { useHistory } from "react-router-dom";
import { Button, Form, Modal, ModalHeader, ModalFooter } from "reactstrap";

const Logout = () => {
    const history = useHistory();

    const handleLogout = () => {
        sessionStorage.clear();
        history.push("/");
        window.location.reload();
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
                </ModalFooter>
            </Form>
        </Modal>
    );
}

export default Logout;