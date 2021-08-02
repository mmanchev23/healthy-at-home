import React, { useState } from 'react';
import style from "./Tasks.module.css";
import { Card, CardBody, CardTitle, Button} from 'reactstrap';
import { useHistory } from 'react-router-dom';

const Task = () => {
    const [tasks, setTasks] = useState([]);
    const history = useHistory();

    if (tasks === undefined) {
        return(
            <div
                style={{
                    display: "grid",
                    justifyContent: "center",
                    alignItems: "center",
                    marginTop: "200px",
                }}
            >
                <h1>No Tasks found!</h1>
                <Button onClick={() => history.push("/task/create")}>Create Task</Button>
            </div>
        );
    } else if(tasks.length === 0) {
        fetch('http://127.0.0.1:8000/tasks/', {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setTasks(data.tasks));
    }

    return(
        <div className={style.parrent}>
            {tasks.map((task) => (
                <Card>
                    <CardBody>
                        <CardTitle tag="h5">{task.title} {
                            task.completed ? "✔" : "❌"
                        }</CardTitle>
                        <CardBody>
                            {task.description}
                        </CardBody>
                        <Button onClick={() => history.push(`/task/${task.id}`)} className={style.button}>Details</Button>
                    </CardBody>
                </Card>
            ))}
        </div>
    )
}

export default Task;