export default function handler(req, res) {
    if (req.method === 'POST') {
      // Process the request here (e.g., send an email, save to a database, etc.)
      // For this example, we'll just return a success message.
      console.log('Received contact form submission:', req.body);
      res.status(200).json({ message: 'Message sent successfully!' });
    } else {
      res.status(405).json({ message: 'Method not allowed' });
    }
  }
  