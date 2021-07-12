import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input } from "reactstrap";

const EditWorkout = (props) => {
    const id = props.match.params.id;
    const [task, setTask] = useState([]);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [completed, setCompleted] = useState(false);
    const history = useHistory();

    if (task === undefined) {
        return "Something went wrong!";
    } else if (task.length === 0) {
        fetch(`https://healthy-at-home2.herokuapp.com/tasks/${id}`, {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setTask(data));
    }

    const handleEdit = (e) => {
        e.preventDefault();

        var myHeaders = new Headers();
        myHeaders.append("Authorization", `Token ${sessionStorage.getItem("key")}`);

        var formdata = new FormData();
        formdata.append("title", title);
        formdata.append("description", description);
        formdata.append("completed", completed);

        var requestOptions = {
            method: 'PUT',
            headers: myHeaders,
            body: formdata,
            redirect: 'follow'
        };

        fetch(`https://healthy-at-home2.herokuapp.com/tasks/${id}/`, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

        setTimeout(() => {
            history.push("/tasks");
            window.location.reload();
        }, 2500);

        toast.success("Task edited successfully...", {
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
        <ModalHeader>Edit "{task.title}"</ModalHeader>
        <ModalBody>
            <Form onSubmit={handleEdit}>
            <FormGroup>
                <Label>Title</Label>
                <Input type="text" onChange={(e) => setTitle(e.target.value)} placeholder={task.title}/>
            </FormGroup>
            <FormGroup>
                <Label>Description</Label>
                <Input type="text" onChange={(e) => setDescription(e.target.value)} placeholder={task.description}/>
            </FormGroup>
            <FormGroup>
                <Input type="checkbox" onChange={(e) => setCompleted(e.target.value)}/>
                Completed
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
