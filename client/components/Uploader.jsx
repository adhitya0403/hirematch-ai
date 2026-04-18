import { useState } from "react";

const Uploader = ({ setContent }) => {
  const [file, setFile] = useState(null);

  const handleUpload = async (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
  };

  const handleFetch = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const url = "http://127.0.0.1:8000";
    try {
      const response = await fetch(`${url}/upload_resume`, {
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setContent(data.text);
    } catch (error) {
      console.log("Fetch Failed", error);
    }
  };

  return (
    <div className="flex items-center justify-center ">
      <div className="border border-gray-800 rounded-xl p-8 w-80 text-center bg-gray-900">
        <h2 className="text-lg font-medium text-gray-200 mb-4">
          Upload Resume
        </h2>

        <label className="block border border-dashed border-gray-700 rounded-lg p-6 cursor-pointer hover:bg-gray-800 transition">
          <input type="file" className="hidden" onChange={handleUpload} />
          <p className="text-sm text-gray-400">Click to upload</p>
        </label>
        <button
          onClick={handleFetch}
          className="bg-green-500 px-4 py-1 mt-2 border-white border-2 rounded-md"
        >
          Next
        </button>
      </div>
    </div>
  );
};

export default Uploader;
