import React, { useState } from 'react';
import style from "./Workouts.module.css";
import { Card, CardImg, CardBody, CardTitle, CardSubtitle, Button } from 'reactstrap';
import { useHistory } from 'react-router-dom';

const Workouts = () => {
    const [workouts, setWorkouts] = useState([]);
    const history = useHistory();

    if (workouts === undefined) {
        return(
            <div
                style={{
                    display: "grid",
                    justifyContent: "center",
                    alignItems: "center",
                    marginTop: "200px",
                }}
            >
                <h1>No workouts found!</h1>
                <Button onClick={() => history.push("/workout/create")}>Create Workout</Button>
            </div>
        );
    } else if(workouts.length === 0) {
        fetch('https://healthy-at-home2.herokuapp.com/workouts/', {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setWorkouts(data.workouts));
    }

    return(
        <div className={style.parrent}>
            {workouts.map((workout) => (
                <Card>
                    <CardImg top src={workout.workout_image} alt="Couldn't load..." />
                    <CardBody>
                        <CardTitle tag="h5">{workout.title}</CardTitle>
                        <CardSubtitle tag="h6" className="mb-2 text-muted">{workout.description}</CardSubtitle>
                        <Button onClick={() => history.push(`/workout/${workout.id}`)} className={style.button}>Check details</Button>
                    </CardBody>
                </Card>
            ))}
        </div>
    )
}

export default Workouts;