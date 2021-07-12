import React, { useState } from 'react';
import { useHistory } from "react-router-dom";
import { ToastContainer, toast, Slide } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { Button, Form, FormGroup, Modal, ModalHeader, ModalBody, ModalFooter, Label, Input } from "reactstrap";

const CreateWorkout = () => {
  const [title, setTitle] = useState("");
  const [workout_image, setWorkoutImage] = useState("");
  const [video_url, setVideoURL] = useState("");
  const [description, setDescription] = useState("");
  const [exercises, setExercises] = useState("");
  const [is_public, setPublic] = useState(false);
  const history = useHistory();
  const [hoverImage, setHoverImage] = useState(false);
  const [hoverVideo, setHoverVideo] = useState(false);

  const onHoverImage = () => {
    setHoverImage(true);
  };

  const onLeaveImage = () => {
    setHoverImage(false);
  };

  const onHoverVideo = () => {
    setHoverVideo(true);
  };

  const onLeaveVideo = () => {
    setHoverVideo(false);
  };

  const handleCreate = (e) => {
    e.preventDefault();

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

    fetch("https://healthy-at-home2.herokuapp.com/workouts/", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));

    setTimeout(() => {
        history.push("/workouts");
        window.location.reload();
    }, 2500);

    toast.success("Workout created successfully...", {
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
      <ModalHeader>Create Workout</ModalHeader>
      <ModalBody>
        <Form onSubmit={handleCreate}>
          <FormGroup>
            <Label>Title</Label>
            <Input type="text" onChange={(e) => setTitle(e.target.value)} placeholder="Enter title"/>
          </FormGroup>
          <FormGroup>
            <Input type="file" onChange={(e) => setWorkoutImage(e.target.value)} placeholder="Enter Image file" onMouseEnter={onHoverImage} onMouseLeave={onLeaveImage}/>
            
          </FormGroup>
          <FormGroup>
            <Label>Video</Label>
            <Input type="link" onChange={(e) => setVideoURL(e.target.value)} placeholder="Enter Video link" onMouseEnter={onHoverVideo} onMouseLeave={onLeaveVideo}/>
            
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
            <Label> Public</Label>
          </FormGroup>
          <FormGroup>
            {hoverImage && <div style={{
              textAlign: "center",
              color: "red",
            }}>Notice! <br></br> If you don't have an image file, <br></br> we will provide default one for you!</div>}
            {hoverVideo && <div style={{
              textAlign: "center",
              color: "red",
            }}>Notice! <br></br> If you don't have a video url, <br></br> we will provide default one for you!</div>}
          </FormGroup>
          <ToastContainer/>
        </Form>
      </ModalBody>
      <ModalFooter>
        <Button color="success" type="submit" onClick={handleCreate} disabled={!(title && description && exercises)}> Create Workout </Button>
        <Button color="danger" type="submit" onClick={handleBack}> Bring me back </Button>
        <ToastContainer/>
      </ModalFooter>
    </Modal>
  )
}

export default CreateWorkout;