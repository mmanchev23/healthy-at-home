import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from "reactstrap";

const Task = (props) => {
    const id = props.match.params.id;
    const [task, setTask] = useState([]);
    const history = useHistory();

    if (task.length === 0) {
        fetch(`http://127.0.0.1:8000/tasks/${id}`, {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setTask(data));
    }

    const handleBack = (e) => {
        e.preventDefault();
        history.goBack();
    }

    return (
        <Modal isOpen={true}>
            <ModalHeader>{task.title}</ModalHeader>
            <ModalBody>
                {task.description}<hr/>
                {task.completed ? "Completed" : "Not Completed"}
            </ModalBody>
            <ModalFooter>
                <Button
                    color="info"
                    type="submit"
                    onClick={() => history.push(`/task/${task.id}/edit`)}>
                    Edit
                </Button>
                <Button
                    color="danger"
                    type="submit"
                    onClick={() => history.push(`/task/${task.id}/delete`)}>
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

export default Task;
