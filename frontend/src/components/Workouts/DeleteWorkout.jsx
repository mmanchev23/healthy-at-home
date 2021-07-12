import React from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import { Button, Form, Modal, ModalHeader, ModalFooter } from "reactstrap";

const DeleteWorkout = (props) => {
    const history = useHistory();
    const id = props.match.params.id;

    const handleDelete = (e) => {
        e.preventDefault();

        fetch(`http://127.0.0.1:8000/api/v1/workouts/${id}`, {
            method: "DELETE",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })

        setTimeout(() => {
            history.push("/workouts");
            window.location.reload();
        }, 2500);

        toast.success("Deleting workout...", {
            transition: Slide,
            position: "top-right",
            autoClose: 2500
        })
    }

    const handleBack = (e) => {
        e.preventDefault();
        history.goBack();
    }

    return(
        <Modal isOpen={true}>
            <Form onSubmit={handleDelete}>
                <ModalHeader>Are you sure?</ModalHeader>
                <ModalFooter>
                    <Button
                        color="success"
                        type="submit"
                        onClick={handleDelete}>
                        Yes, delete the workout
                    </Button>
                    <Button
                        color="danger"
                        type="submit"
                        onClick={handleBack}>
                        No, bring me back
                    </Button>
                    <ToastContainer/>
                </ModalFooter>
            </Form>
        </Modal>
    );
}

export default DeleteWorkout;
