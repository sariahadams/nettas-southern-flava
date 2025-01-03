"use client";

import React, { useEffect } from "react";
import api from "../api";

const ExampleComponent = () => {

    const pingBackend = async () => {
        const response = await api.get();
        console.log(response.data);
    };
    
    // Ping the backend
    useEffect(() => {
        pingBackend();
    }, []);

    return <div>Pinged Backend! See the console...</div>;
};

export default ExampleComponent;