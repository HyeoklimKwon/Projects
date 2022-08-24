import firebase from "firebase/app";
import "firebase/database";


const config = {
    // API KEYS
    apiKey: "AIzaSyBprNH2vg4DOYfz7tt9diRu1h_zQq6nHTg",
    authDomain: "firevuechat-fcecc.firebaseapp.com",
    projectId: "firevuechat-fcecc",
    storageBucket: "firevuechat-fcecc.appspot.com",
    messagingSenderId: "297412001469",
    appId: "1:297412001469:web:06584bb7cc7a04626d81d4"
}

const db = firebase.initializeApp(config);
export default db;