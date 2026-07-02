import { use, useState } from "react";

export default function QuizGenerator() {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [quiz, setQuiz] = useState(null);

    const handleUpload = async () => {
        if (!file) return;
        setLoading(true);

        const formData = new FormData();
        formData.append('file', file);

        const uploadRes = await fetch('/api/upload', {method: 'POST', body: formData});
        const {extracted_text} = await uploadRes.json();

        const genRes = await fetch('/api/assignments/generate-quiz', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({text: extracted_text})
        });

        const quizData = await genRes.json();
        setQuiz(quizData);
        setLoading(false);
    };

    return (
        <div className="p-4 border rounded shadow">
            <h2 className="text-xl mb-4">Magic Curriculum Quiz Generator</h2>
            <input type="file" onChange={(e) => setFile(e.target.files?.[0] || null)} />
            <button onClick={handleUpload} className="bg-teal-500 text-white px-4 py-2 mt-4 rounded">
                {loading ? 'Generating...': 'Generate Quiz'}
            </button>

            {quiz && (
                <div className="mt-4">
                    <h3 className="font-bold">Preview</h3>
                    <pre className="text-sm bg-gray-100 p-2">{JSON.stringify(quiz, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}