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
      {content.resume_sections && (
        <div className="space-y-6">
          {Object.entries(content?.resume_sections || {}).map(
            ([section, items]) => (
              <div key={section}>
                <h2 className="font-semibold text-green-400 mb-2 capitalize">
                  {section}
                </h2>

                <div className="flex flex-wrap gap-2">
                  {items.map((item, i) => (
                    <span
                      key={i}
                      className="text-sm text-gray-300 px-2 py-1 border border-gray-700 rounded"
                    >
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            ),
          )}
        </div>
      )}

      {content.jd_set && (
        <div>
          <h2 className="font-semibold text-blue-400 mb-1">Job Description</h2>
          <div className="flex flex-wrap gap-2">
            {content?.jd_set?.map((word) => (
              <span key={word} className="text-sm text-gray-300 px-2 py-1">
                {word}
              </span>
            ))}
          </div>
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

export default Viewer;
