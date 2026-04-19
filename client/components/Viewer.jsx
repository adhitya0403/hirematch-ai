const Viewer = ({ content }) => {
  if (!content) return null;

  if (content.error) {
    return (
      <div className="border-2 border-red-500 p-5 text-red-400">
        {content.error}
      </div>
    );
  }

  return (
    <div className="border-2 border-dotted border-gray-700 rounded-md p-6 space-y-4 text-white">

      {content.resume_text && (
        <div>
          <h2 className="font-semibold text-green-400 mb-1">Resume</h2>
          <p className="text-sm whitespace-pre-wrap">
            {content.resume_text}
          </p>
        </div>
      )}

      {content.jd_text && (
        <div>
          <h2 className="font-semibold text-blue-400 mb-1">Job Description</h2>
          <p className="text-sm whitespace-pre-wrap">
            {content.jd_text}
          </p>
        </div>
      )}

      {content.role && (
        <div>
          <h2 className="font-semibold text-yellow-400 mb-1">Role</h2>
          <p className="text-sm">{content.role}</p>
        </div>
      )}
    </div>
  );
};

export default Viewer