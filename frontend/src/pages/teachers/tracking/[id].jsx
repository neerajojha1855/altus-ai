import { useEffect, useState } from "react";
import { useRouter } from "next/router";

export default function SubmissionTracking() {
    const router = useRouter();
    const {id} = router.query();
    const {tracking, setTracking} = useState();

    useEffect(() => {
        if(id) {
            fetch(`/api/assignments/${id}/tracking`, {
                headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}
            })
            .then(res => res.json())
            .then(data => setTracking(data));
        }
    }, [id]);

    const handleRemind = async (studentId) => {
        await fetch(`/api/assignments/${id}/remind`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify({student_ids: [studentId]})
        });
        alert('Reminder sent!');
    };

    return (
        <div className="p-8">
            <h1 className="text-2xl font-bold mb-4">Submission Tracking</h1>
            <ul className="space-y-4">
                {tracking.map((student) => (
                    <li key={student.student_id} className="flex items-center justify-between p-4 border rounded">
                        <div>
                            <p className="font-bold">{student.student_name}</p>
                            <span className={`text-sm ${student.status === 'missing' ? 'text-red-500' : 'text-green-500'}`}>
                                {student.status.toUpperCase()}
                            </span>
                        </div>
                        {student.status === 'missing' && (
                            <button 
                                onClick={() => handleRemind(student.student_id)}
                                className="bg-yellow-500 text-white px-4 py-2 rounded"
                            >
                                Send Reminder
                            </button>
                        )}
                    </li>
                ))}
            </ul>
        </div>
    );
}