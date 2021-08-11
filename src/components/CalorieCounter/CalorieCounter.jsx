import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { Button, Form, Modal, ModalHeader, ModalFooter, ModalBody } from "reactstrap";

const CalorieCounter = () => {
    const [user, setUser] = useState([]);
    const history = useHistory();

    if (user.length === 0) {
        fetch("http://127.0.0.1:8000/credentials/", {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(response => response.json())
        .then(data =>setUser(data.credentials[0]))
    }

    const calculateBMI = () => {
        history.push("/bmi");
    }
    
    const addFood = () => {
        history.push("/meals");
    }

    const goBack = (e) => {
        e.preventDefault();
        history.goBack();
    }

    return (
        <Modal isOpen={true}>
            <Form>
                <ModalHeader>Daily Intake</ModalHeader>
                <ModalBody>
                    <ul>
                        <li>Calories: {user.total_calories}</li>
                        <li>Fat: {user.total_fat}</li>
                        <li>Proteins: {user.total_proteins}</li>
                        <li>Carbs: {user.total_carbs}</li>
                    </ul>
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" type="submit" onClick={calculateBMI}>Calculate BMI</Button>
                    <Button color="success" type="submit" onClick={addFood}>Meals</Button>
                    <Button color="danger" type="submit" onClick={goBack}>Bring me back</Button>
                </ModalFooter>
            </Form>
        </Modal>
    );
}

export default CalorieCounter;
