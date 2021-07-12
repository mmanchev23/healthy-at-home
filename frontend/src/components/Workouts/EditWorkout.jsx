import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input } from "reactstrap";

const EditWorkout = (props) => {
    const id = props.match.params.id;
    const [workout, setWorkout] = useState([]);
    const [title, setTitle] = useState("");
    const [workout_image, setWorkoutImage] = useState("");
    const [video_url, setVideoURL] = useState("");
    const [description, setDescription] = useState("");
    const [exercises, setExercises] = useState("");
    const [is_public, setPublic] = useState(false);
    const history = useHistory();

    if (workout === undefined) {
        return "Something went wrong!";
    } else if (workout.length === 0) {
        fetch(`https://healthy-at-home2.herokuapp.com/workouts/${id}`, {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setWorkout(data));
    }

    const handleEdit = (e) => {
        e.preventDefault();

        var myHeaders = new Headers();
        myHeaders.append("Authorization", `Token ${sessionStorage.getItem("key")}`);

        var formdata = new FormData();
        formdata.append("title", title);
        formdata.append("workout_image", workout_image);
        formdata.append("description", description);
        formdata.append("exercises", exercises);
        formdata.append("video_url", video_url);
        formdata.append("public", is_public);

        var requestOptions = {
            method: 'PUT',
            headers: myHeaders,
            body: formdata,
            redirect: 'follow'
        };

        fetch(`https://healthy-at-home2.herokuapp.com/workouts/${id}/`, requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));

        setTimeout(() => {
            history.push("/workouts");
            window.location.reload();
        }, 2500);

        toast.success("Workout edited successfully...", {
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
        <ModalHeader>Edit "{workout.title}"</ModalHeader>
        <ModalBody>
            <Form onSubmit={handleEdit}>
            <FormGroup>
                <Label>Title</Label>
                <Input type="text" onChange={(e) => setTitle(e.target.value)} placeholder={workout.title}/>
            </FormGroup>
            <FormGroup>
                <Input type="file" onChange={(e) => setWorkoutImage(e.target.value)}  placeholder={workout.workout_image}/>
            </FormGroup>
            <FormGroup>
                <Label>Video</Label>
                <Input type="link" onChange={(e) => setVideoURL(e.target.value)} placeholder={workout.video_url}/>
            </FormGroup>
            <FormGroup>
                <Label>Description</Label>
                <Input type="text" onChange={(e) => setDescription(e.target.value)} placeholder={workout.description}/>
            </FormGroup>
            <FormGroup>
                <Label>Exercises</Label>
                <Input type="text" onChange={(e) => setExercises(e.target.value)} placeholder={workout.exercises}/>
            </FormGroup>
            <FormGroup>
                <Label>Public: </Label>
                <Input type="checkbox" onChange={(e) => setPublic(e.target.value)} checked={workout.is_public}/>
            </FormGroup>
            <ToastContainer/>
            </Form>
        </ModalBody>
        <ModalFooter>
            <Button color="success" type="submit" onClick={handleEdit} disabled={!(title && description && exercises)}>Save changes</Button>
            <Button color="danger" type="submit" onClick={handleBack}>Bring me back</Button>
            <ToastContainer/>
        </ModalFooter>
        </Modal>
    )
}

export default EditWorkout
