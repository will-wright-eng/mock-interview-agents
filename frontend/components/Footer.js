const Footer = () => {
  return (
    <footer className="footer p-4 bg-base-200 text-base-content footer-center">
      <div>
        <p>© 2024 MyPortfolio - All rights reserved</p>
        <div className="flex space-x-4">
          <a href="#" className="btn btn-ghost"><i className="fab fa-twitter"></i></a>
          <a href="#" className="btn btn-ghost"><i className="fab fa-linkedin"></i></a>
          <a href="#" className="btn btn-ghost"><i className="fab fa-github"></i></a>
        </div>
      </div>
    </footer>
  );
}
export default Footer;
