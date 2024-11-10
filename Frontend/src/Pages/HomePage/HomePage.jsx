import React from "react";
import './HomePage.css';
import LogoPng from '../../assets/logo.png'

const HomePage = () => {
    const GrabImage = () => {
        alert("Div clicked!");
    }
    return(
        <>
            <div className="HomePageContainer">
                <div className="TextContainer">
                    <div className="Welcome">
                        <p>Certifed Compiler Boys Bring You:</p>
                        <p className="CompanyName">Vybe-Fynd3r</p>
                    </div>
                    <div class="CatchPhrase">
                        Vision To Vibes
                    </div>
                </div>
                <div className="ImageContainer">
                    <div className="ImgCont" onClick={GrabImage}>
                        <img src={LogoPng}/>
                    </div>
                </div>
            </div>
        </>
    )

}

export default HomePage;
