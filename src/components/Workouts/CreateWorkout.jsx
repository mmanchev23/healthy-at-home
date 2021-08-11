import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input } from "reactstrap";

const CreateWorkout = () => {
  const history = useHistory();
  const [title, setTitle] = useState("");
  const [workout_image, setWorkoutImage] = useState("");
  const [video_url, setVideoURL] = useState("");
  const [description, setDescription] = useState("");
  const [exercises, setExercises] = useState("");
  const [is_public, setPublic] = useState(false);

  const handleCreate = async e => {
    e.preventDefault();

    // await axios.post("http://127.0.0.1:8000/workouts/",
    // {
    //   headers: {
    //     'Content-Type': 'application/json',
    //     'Authorization': `Token ${sessionStorage.getItem("key")}`
    //   },
    //   body: {
    //     "title": title,
    //     "workout_image": workout_image,
    //     "video_url": video_url,
    //     "description": description,
    //     "exercises": exercises,
    //     "video_url": video_url,
    //     "public": is_public
    //   },
    //   redirect: 'follow'
    // })
    // .then(response => {
    //   console.log(response);

    //   toast.success("Workout created successfully...", {
    //       transition: Slide,
    //       position: "top-right",
    //       autoClose: 2500
    //   });

    //   setTimeout(() => {
    //       history.push("/workouts");
    //       window.location.reload();
    //   }, 2500);
    // })
    // .catch(error => {
    //   console.log(error);
      
    //   toast.error("An error occured! Please try again...", {
    //     transition: Slide,
    //     position: "top-right",
    //     autoClose: 2500
    //   });
    // });

    var myHeaders = new Headers();
    myHeaders.append("Authorization", `Token ${sessionStorage.getItem("key")}`);

    var formdata = new FormData();
    formdata.append("title", title);
    formdata.append("workout_image", workout_image);
    formdata.append("video_url", video_url);
    formdata.append("description", description);
    formdata.append("exercises", exercises);
    formdata.append("video_url", video_url);
    formdata.append("public", is_public);

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: formdata,
        redirect: 'follow'
    };

    fetch("http://127.0.0.1:8000/workouts/", requestOptions)
    .then(response => response.text())
    .then(result => {
      console.log(result);
      toast.success("Workout created successfully...", {
        transition: Slide,
        position: "top-right",
        autoClose: 2500
      });
    
      setTimeout(() => {
        history.push("/workouts");
        window.location.reload();
      }, 2500);
    })
    .catch(error => {
      console.log(error);
      toast.error("An error occured! Please try again...", {
        transition: Slide,
        position: "top-right",
        autoClose: 2500
      });
    });
  }

  const handleBack = (e) => {
    e.preventDefault();
    history.goBack();
  }

  return(
    <Modal isOpen={true}>
      <ModalHeader>Create Workout</ModalHeader>
      <ModalBody>
        <Form onSubmit={handleCreate}>
          <FormGroup>
            <Label>Title</Label>
            <Input type="text" onChange={(e) => setTitle(e.target.value)} placeholder="Enter title"/>
          </FormGroup>
          <FormGroup>
            <Input type="file" onChange={(e) => setWorkoutImage(e.target.value)} placeholder="If you don't have an image, we will provide a default one for you."/>
          </FormGroup>
          <FormGroup>
            <Label>Video</Label>
            <Input type="link" onChange={(e) => setVideoURL(e.target.value)} placeholder="If you don't have a video, we will provide a default one for you."/>
          </FormGroup>
          <FormGroup>
            <Label>Description</Label>
            <Input type="text" onChange={(e) => setDescription(e.target.value)} placeholder="Enter description"/>
          </FormGroup>
          <FormGroup>
            <Label>Exercises</Label>
            <Input type="text" onChange={(e) => setExercises(e.target.value)} placeholder="Enter exercises"/>
          </FormGroup>
          <FormGroup>
            <Input type="checkbox" onChange={(e) => setPublic(e.target.value)}/>
            <Label>Public</Label>
          </FormGroup>
          <ToastContainer/>
        </Form>
      </ModalBody>
      <ModalFooter>
        <Button color="success" type="submit" onClick={handleCreate} disabled={!(title && description && exercises)}>Create Workout</Button>
        <Button color="danger" type="submit" onClick={handleBack}> Bring me back </Button>
        <ToastContainer/>
      </ModalFooter>
    </Modal>
  )
}

export default CreateWorkout;