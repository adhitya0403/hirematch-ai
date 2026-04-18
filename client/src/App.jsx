import React from "react";
import Uploader from "../components/Uploader.jsx";
import { useState } from "react";
import Viewer from "../components/Viewer.jsx";

const App = () => {
  const [content, setContent] = useState("content");
  return (
    <div className="h-dvh w-full flex justify-center items-center bg-gray-950 gap-15">
      <Uploader setContent={setContent}/>
      <Viewer content={content}/>
    </div>
  );
};

export default App;
