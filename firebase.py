from firebase import firebase


fb = firebase.FirebaseApplication('https://fir-webapp-86964.firebaseio.com/', None)
fb.put('Users',"Current_Floor",6)
