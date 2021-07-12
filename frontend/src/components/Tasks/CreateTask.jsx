import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input } from "reactstrap";

const EditWorkout = () => {
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [completed, setCompleted] = useState(false);
    const history = useHistory();

    const handleEdit = (e) => {
        e.preventDefault();

        var myHeaders = new Headers();
        myHeaders.append("Authorization", `Token ${sessionStorage.getItem("key")}`);

        var formdata = new FormData();
        formdata.append("title", title);
        formdata.append("description", description);
        formdata.append("completed", completed);

        var requestOptions = {
            method: 'POST',
            headers: myHeaders,
            body: formdata,
            redirect: 'follow'
        };

        fetch(`https://healthy-at-home2.herokuapp.com/tasks/`, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

        setTimeout(() => {
            history.push("/tasks");
            window.location.reload();
        }, 2500);

        toast.success("Task created successfully...", {
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
        <ModalHeader>Create Task</ModalHeader>
        <ModalBody>
            <Form onSubmit={handleEdit}>
            <FormGroup>
                <Label>Title</Label>
                <Input type="text" onChange={(e) => setTitle(e.target.value)} placeholder="Enter title"/>
            </FormGroup>
            <FormGroup>
                <Label>Description</Label>
                <Input type="text" onChange={(e) => setDescription(e.target.value)} placeholder="Enter description"/>
            </FormGroup>
            <FormGroup>
                <Input type="checkbox" onChange={(e) => setCompleted(e.target.value)}/>
                <Label>Completed</Label>
            </FormGroup>
            <ToastContainer/>
            </Form>
        </ModalBody>
        <ModalFooter>
            <Button color="success" type="submit" onClick={handleEdit} disabled={!(title && description)}>Save changes</Button>
            <Button color="danger" type="submit" onClick={handleBack}>Bring me back</Button>
            <ToastContainer/>
        </ModalFooter>
        </Modal>
    )
}

export default EditWorkout