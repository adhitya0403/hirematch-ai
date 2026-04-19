import { useState } from "react";

export default function Uploader({setContent}) {
  const [mode, setMode] = useState("resume_only");

  const [resume, setResume] = useState(null);

  const [jdType, setJdType] = useState("file");
  const [jdFile, setJdFile] = useState(null);
  const [jdText, setJdText] = useState("");

  const [role, setRole] = useState("");

  const handleAnalyze = async () => {
    if (!resume) return alert("Upload resume first");

    if (mode === "resume_jd") {
      if (jdType === "file" && !jdFile) return alert("Upload JD file");
      if (jdType === "text" && !jdText.trim()) return alert("Paste JD text");
    }

    const formData = new FormData();

    // always send resume
    formData.append("resume", resume);

    // JD handling
    if (mode === "resume_jd") {
      if (jdType === "file") {
        formData.append("jd_file", jdFile);
      } else {
        formData.append("jd_text", jdText);
      }
    }

    // role (only resume mode)
    if (mode === "resume_only" && role) {
      formData.append("role", role);
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setContent(data)
    } catch (err) {
      console.log("Error:", err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center text-white px-4">
      <div className="w-full max-w-lg bg-gray-900 border border-gray-800 rounded-xl p-6 space-y-6">
        {/* Title */}
        <div>
          <h1 className="text-xl font-semibold">Resume Analyzer</h1>
          <p className="text-sm text-gray-400">
            Analyze your resume with or without a job description
          </p>
        </div>

        {/* Mode Switch */}
        <div className="flex bg-gray-800 rounded-lg p-1">
          <button
            onClick={() => {
              setMode("resume_only");
              setJdFile(null);
              setJdText("");
            }}
            className={`flex-1 py-2 text-sm rounded-md ${
              mode === "resume_only"
                ? "bg-green-500 text-black"
                : "text-gray-400"
            }`}
          >
            Resume Only
          </button>

          <button
            onClick={() => setMode("resume_jd")}
            className={`flex-1 py-2 text-sm rounded-md ${
              mode === "resume_jd" ? "bg-green-500 text-black" : "text-gray-400"
            }`}
          >
            Resume + JD
          </button>
        </div>

        {/* Resume Upload */}
        <div>
          <p className="text-sm mb-2 text-gray-300">Resume</p>
          <label className="block border border-dashed border-gray-700 rounded-lg p-5 text-center cursor-pointer hover:bg-gray-800 transition">
            <input
              type="file"
              accept=".pdf,.docx,.txt"
              className="hidden"
              onChange={(e) => setResume(e.target.files[0])}
            />
            <p className="text-sm text-gray-400">
              {resume ? "✅ " + resume.name : "Click to upload resume"}
            </p>
          </label>
        </div>

        {/* JD Section */}
        {mode === "resume_jd" && (
          <div className="space-y-3">
            <p className="text-sm text-gray-300">Job Description</p>

            {/* JD Type Toggle */}
            <div className="flex gap-2">
              <button
                onClick={() => {
                  setJdType("file");
                  setJdText("");
                }}
                className={`px-3 py-1 rounded-md text-sm ${
                  jdType === "file"
                    ? "bg-green-500 text-black"
                    : "bg-gray-800 text-gray-400"
                }`}
              >
                Upload File
              </button>

              <button
                onClick={() => {
                  setJdType("text");
                  setJdFile(null);
                }}
                className={`px-3 py-1 rounded-md text-sm ${
                  jdType === "text"
                    ? "bg-green-500 text-black"
                    : "bg-gray-800 text-gray-400"
                }`}
              >
                Paste Text
              </button>
            </div>

            {/* JD Input */}
            {jdType === "file" ? (
              <label className="block border border-dashed border-gray-700 rounded-lg p-5 text-center cursor-pointer hover:bg-gray-800 transition">
                <input
                  type="file"
                  accept=".pdf,.docx,.txt"
                  className="hidden"
                  onChange={(e) => setJdFile(e.target.files[0])}
                />
                <p className="text-sm text-gray-400">
                  {jdFile ? "✅ " + jdFile.name : "Upload JD file"}
                </p>
              </label>
            ) : (
              <textarea
                placeholder="Paste job description here..."
                value={jdText}
                onChange={(e) => setJdText(e.target.value)}
                className="w-full h-32 p-3 bg-gray-800 border border-gray-700 rounded-md text-sm focus:outline-none focus:border-green-500"
              />
            )}
          </div>
        )}

        {/* Role Input (only resume mode) */}
        {mode === "resume_only" && (
          <input
            type="text"
            placeholder="Target Role (optional)"
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="w-full px-3 py-2 rounded-md bg-gray-800 border border-gray-700 text-sm outline-none focus:border-green-500"
          />
        )}

        {/* Button */}
        <button
          onClick={handleAnalyze}
          disabled={
            !resume ||
            (mode === "resume_jd" &&
              (jdType === "file" ? !jdFile : !jdText.trim()))
          }
          className="w-full py-2 rounded-md bg-green-500 text-black font-medium disabled:opacity-50"
        >
          {mode === "resume_jd" ? "Compare" : "Analyze"}
        </button>
      </div>
    </div>
  );
}
