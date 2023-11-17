<template>
    <div>
      <h1>Edit Profile</h1>
      <form @submit.prevent="updateProfile">
        <div>
          <label for="email">Email:</label>
          <input v-model="user.email" type="email" id="email" />
        </div>
        <div>
          <label for="dob">Date of Birth:</label>
          <input v-model="user.date_of_birth" type="date" id="dob" />
        </div>
        <div>
          <label for="image">Profile Image:</label>
          <input type="file" id="image" @change="onFileChange" />
        </div>
        <button type="submit">Update Profile</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          email: '',
          date_of_birth: '',
          profile_image: null,
        },
      };
    },
    methods: {
      onFileChange(e) {
        this.user.profile_image = e.target.files[0];
      },
      async updateProfile() {
        const formData = new FormData();
        formData.append('email', this.user.email);
        formData.append('date_of_birth', this.user.date_of_birth);
        if (this.user.profile_image) {
          formData.append('profile_image', this.user.profile_image);
        }
  
        try {
          const response = await fetch('/api/update-profile/', {
            method: 'POST',
            body: formData,
            credentials: 'include', // if you're using session-based authentication
          });
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          // Handle success, e.g., show a success message, redirect, etc.
        } catch (error) {
          // Handle error, e.g., show an error message
        }
      },
    },
  };
  </script>
  