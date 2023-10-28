// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Import the functions you need from the SDKs you need
import firebase from "firebase/compat/app";
import "firebase/compat/database";
import {getAuth, GoogleAuthProvider} from "firebase/auth";
// import { getAuth, GoogleAuthProvider } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyA8J3VgdKz1NV1QVkp1xUMSIdbIDk8v4B8",
  authDomain: "foodkingdom-833bf.firebaseapp.com",
  projectId: "foodkingdom-833bf",
  storageBucket: "foodkingdom-833bf.appspot.com",
  messagingSenderId: "685888313162",
  appId: "1:685888313162:web:396321981a5c6390ea13b3",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
// const app = initializeApp(firebaseConfig);
const database = firebase.database();
const auth = getAuth();
const provider = new GoogleAuthProvider();

export {firebase, auth, database,provider};