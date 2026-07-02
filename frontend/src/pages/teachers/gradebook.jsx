import {useEffect, useState} from 'react';

export default function Gradebook() {
    const [submissions, setSubmissions] = useState([]);

    useEffect(() => {
        fetch('/api/classes/1/gradebook', {
            headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}
        })
        .then(res => res.json())
        .then(data => setSubmissions(data));
    }, []);

    return (
        <div className="p-8">
            <h1 className="text-2xl font-bold mb-4">Gradebook</h1>
            <table className='min-w-full bg-white border'>
                <thead>
                    <tr>
                        <th className='border p-2'>Student</th>
                        <th className='border p-2'>Assignment</th>
                        <th className='border p-2'>Score</th>
                        <th className='border p-2'>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {submissions.map((sub) => {
                        <tr key={sub.id}>
                            <td className='border p-2'>{sub.student_name}</td>
                            <td className='border p-2'>{sub.assignment_title}</td>
                            <td className='border p-2'>{sub.score}</td>
                            <td className='border p-2 text-green-600'>Graded</td>
                        </tr>
                    })}
                </tbody>
            </table>
        </div>
    );
}