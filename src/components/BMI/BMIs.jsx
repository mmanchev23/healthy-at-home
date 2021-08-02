import React, { useState } from 'react';
import style from "./BMI.module.css";
import { useHistory } from 'react-router-dom';
import { Card, CardBody, CardTitle, Button} from 'reactstrap';

const BMIs = () => {
    const [results, setResult] = useState([]);
    const history = useHistory();

    if (results === undefined) {
        return(
            <div
                style={{
                    display: "grid",
                    justifyContent: "center",
                    alignItems: "center",
                    marginTop: "200px",
                }}
            >
                <h1>No Results found!</h1>
                <Button onClick={() => history.push("/bmi/create")}>Create BMI</Button>
            </div>
        );
    } else if(results.length === 0) {
        fetch('http://127.0.0.1:8000/bmi/', {
            method: "GET",
            headers: {
                'Authorization': `Token ${sessionStorage.getItem("key")}`
            }
        })
        .then(result => result.json())
        .then(data => setResult(data.result));
    }

    return(
        <div className={style.parrent}>
            {results.map((result) => (
                <Card>
                    <CardBody>
                        <CardTitle tag="h5">{result.title} {
                            result.completed ? "✔" : "❌"
                        }</CardTitle>
                        <CardBody>
                            {result.description}
                        </CardBody>
                        <Button onClick={() => history.push(`/bmi/${result.id}`)} className={style.button}>Details</Button>
                    </CardBody>
                </Card>
            ))}
        </div>
    );
}

export default BMIs
