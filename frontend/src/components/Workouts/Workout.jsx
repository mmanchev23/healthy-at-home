import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from "reactstrap";

const Workout = (props) => {
    const id = props.match.params.id;
    const [workout, setWorkout] = useState([]);
    const history = useHistory();

    if (workout.length === 0) {
        fetch(`http://127.0.0.1:8000/api/v1/workouts/${id}`, {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setWorkout(data));
    }

    const handleBack = (e) => {
        e.preventDefault();
        history.goBack();
    }

    return (
        <Modal isOpen={true}>
            <ModalHeader>{workout.title}</ModalHeader>
            <ModalBody>
                <iframe title="video" width="100%" height="400px" src={workout.video_url}/>
                <div>{workout.exercises}</div>
            </ModalBody>
            <ModalFooter>
                <Button
                    color="info"
                    type="submit"
                    onClick={() => history.push(`/workout/${workout.id}/edit`)}>
                    Edit
                </Button>
                <Button
                    color="danger"
                    type="submit"
                    onClick={() => history.push(`/workout/${workout.id}/delete`)}>
                    Delete
                </Button>
                <Button
                    color="success"
                    type="submit"
                    onClick={handleBack}>
                    Back
                </Button>
            </ModalFooter>
        </Modal>
    )
}

export default Workout;
